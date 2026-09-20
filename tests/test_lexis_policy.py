# Copyright © 2026 Chelsea Megan Woods
from src.agent import LexisAgent


def test_lexis_never_claims_formal_advice():
    agent = LexisAgent()
    findings = agent.review("unlimited liability and indemnification")
    assert all(f.formal_legal_advice is False for f in findings)
    assert any(f.severity == "high" for f in findings)
