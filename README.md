# Website Health Monitor

## Overview

Website Health Monitor is a Flask based monitoring application that tracks website availability, response latency, and HTTP status information.

The system continuously checks target websites and records monitoring data for troubleshooting and analysis.

## Problem Statement

Organizations need to ensure that websites remain available and responsive.

Website Health Monitor helps identify outages, performance issues, and response failures by performing automated health checks.

## Features

* Website availability monitoring
* Response latency measurement
* HTTP status tracking
* URL validation
* Monitoring logs
* Error handling
* Historical tracking
* REST API endpoints

## Tech Stack

* Python
* Flask
* SQLite
* Requests Library
* Git

## Architecture

Client Request
↓
Flask Route
↓
Monitoring Service
↓
HTTP Request
↓
Response Analysis
↓
SQLite Storage

## Health Check Workflow

1. User submits website URL.
2. Application validates URL.
3. HTTP request is sent.
4. Response status is collected.
5. Response latency is calculated.
6. Results are stored in database.
7. Monitoring information is returned.

## HTTP Status Examples

* 200 : Success
* 301 : Redirect
* 404 : Not Found
* 500 : Internal Server Error

## Logging Information

Stored information includes:

* URL
* Timestamp
* Status Code
* Response Time
* Error Message

## Learning Outcomes

* Flask application development
* HTTP protocol understanding
* Monitoring system design
* REST API development
* Logging and troubleshooting

## Future Improvements

* Real-time dashboard
* Email alerts
* SMS notifications
* Multi-site monitoring
* Scheduled monitoring jobs
* Cloud deployment
