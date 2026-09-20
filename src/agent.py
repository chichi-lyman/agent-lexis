# Copyright © 2026 Chelsea Megan Woods
"""Agent Lexis — compliance risk flags (no formal legal advice)."""

from __future__ import annotations

from pydantic import BaseModel, Field


class RiskFinding(BaseModel):
    severity: str  # low | medium | high
    clause_hint: str
    recommendation: str
    formal_legal_advice: bool = Field(default=False)


class LexisAgent:
    name = "agent_lexis"

    def review(self, text: str) -> list[RiskFinding]:
        findings: list[RiskFinding] = []
        lower = text.lower()
        if "indemnif" in lower or "unlimited liability" in lower:
            findings.append(
                RiskFinding(
                    severity="high",
                    clause_hint="liability / indemnity",
                    recommendation="Human counsel review required before execution",
                )
            )
        if not findings:
            findings.append(
                RiskFinding(
                    severity="low",
                    clause_hint="general",
                    recommendation="No high-severity patterns detected; still not formal legal advice",
                )
            )
        return findings
