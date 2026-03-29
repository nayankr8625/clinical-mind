# ClinicalMind

> Autonomous competitive intelligence for clinical trials.

---

## What is ClinicalMind?

ClinicalMind continuously monitors global clinical trial registries, FDA correspondence, and investor disclosures — then uses an AI reasoning agent to deliver plain-English competitive intelligence briefs to pharmaceutical and biotech teams.

The core insight: **the signal is not in the data. It's in the delta.**

What changed in a competitor's trial protocol, why it probably changed, and what it means for your program — that's the question no existing tool answers automatically.

---

## Why we're building this

A typical pharma competitive intelligence analyst spends **20–40 hours per week** manually:

- Checking ClinicalTrials.gov for protocol updates across 50–80 competitor trials
- Comparing current vs. previous trial versions side by side
- Interpreting what changes mean in clinical and competitive context
- Writing summaries and posting them to Slack or email

Existing platforms (Citeline, Evaluate Pharma, GlobalData) are expensive databases. They show you *current state* — not *what changed*, *why it changed*, or *what it implies for a competing program*.

ClinicalMind automates the entire workflow:

1. **Detects** meaningful changes — protocol amendments, enrollment pauses, endpoint modifications, early terminations
2. **Reasons** about what each change means using a multi-step AI agent
3. **Delivers** structured intelligence briefs via dashboard, email, Slack, or Claude Desktop

---

## Who it's for

| User | Role |
|------|------|
| CI Analyst | Monitors 50–80 competitor trials weekly |
| Head of CI | Oversees multi-TA competitive intelligence team |
| Biotech Strategy | CEO/CSO who can't afford $40–200k/yr legacy tools |
| Healthcare VC | Partner needing competitor failure signals before market pricing |

---

## Stack

Python · FastAPI · LangGraph · PostgreSQL · pgvector · Next.js · MCP Python SDK · Celery · Redis

---

## Getting started

```bash
# Copy environment config
cp .env.example .env
# Edit .env with your API keys

# Start all services
docker compose up
```

The API will be available at `http://localhost:8000` and the dashboard at `http://localhost:3000`.

---

## License

See [LICENSE](LICENSE).
