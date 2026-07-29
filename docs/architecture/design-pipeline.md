# Pipeline Architecture Diagram


## Diagram
```mermaid
flowchart LR
    A[Source Data] -->|Ingest| B(Bronze: Files)
    B -->|Clean & Validate| C{Data Quality}
    C -->|Pass| D(Silver: Cleansed Tables)
    C -->|Fail| E[Error Log]
    D -->|Transform| F(Gold: Data Model)
    F -->|Deliver| G[Final Output: Dashboard]
```

```mermaid
flowchart LR
    Source[Source data] --> Bronze[Bronze layer]
    Bronze --> Silver[Silver layer]
    Silver --> Gold[Gold layer]
```

## Questions to answer:

### One design decision
- We decided to decouple data validation from ingestion by storing raw data in its orignal form in the Bronze layer. All data cleansing was done in the silver layer.

### One question or risk
- We are unsure about the volume of data we need to process for this pipeline.
