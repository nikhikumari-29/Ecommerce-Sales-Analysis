-- CREATE DATABASE ecommerce_sales;
USE ecommerce_sales;
-- CREATE TABLE superstore (
--     Row_ID INT,
--     Order_ID VARCHAR(50),
--     Order_Date DATE,
--     Ship_Date DATE,
--     Ship_Mode VARCHAR(50),
--     Customer_ID VARCHAR(50),
--     Customer_Name VARCHAR(100),
--     Segment VARCHAR(50),
--     Country VARCHAR(50),
--     City VARCHAR(100),
--     State VARCHAR(100),
--     Postal_Code VARCHAR(20),
--     Region VARCHAR(50),
--     Product_ID VARCHAR(50),
--     Category VARCHAR(50),
--     Sub_Category VARCHAR(50),
--     Product_Name VARCHAR(255),
--     Sales DECIMAL(10,2),
--     Quantity INT,
--     Discount DECIMAL(5,2),
--     Profit DECIMAL(10,2)
-- );
-- SHOW TABLES;
-- SELECT COUNT(*) FROM superstore;
-- DROP TABLE superstore;
-- CREATE TABLE superstore (
--     Row_ID INT,
--     Order_ID VARCHAR(50),
--     Order_Date VARCHAR(20),
--     Ship_Date VARCHAR(20),
--     Ship_Mode VARCHAR(50),
--     Customer_ID VARCHAR(50),
--     Customer_Name VARCHAR(100),
--     Segment VARCHAR(50),
--     Country VARCHAR(50),
--     City VARCHAR(100),
--     State VARCHAR(100),
--     Postal_Code VARCHAR(20),
--     Region VARCHAR(50),
--     Product_ID VARCHAR(50),
--     Category VARCHAR(50),
--     Sub_Category VARCHAR(50),
--     Product_Name VARCHAR(255),
--     Sales DECIMAL(10,2),
--     Quantity INT,
--     Discount DECIMAL(5,2),
--     Profit DECIMAL(10,2)
-- );
USE ecommerce_sales;

-- SELECT * FROM superstore
-- LIMIT 5;
-- SELECT SUM(Sales) AS Total_Sales
-- FROM superstore;
-- SELECT COUNT(*) AS Total_Rows,
-- SUM(Sales) AS Total_Sales,
-- SUM(Profit) AS Total_Profit
-- FROM superstore;
-- SELECT COUNT(DISTINCT order_ID) AS Total_Orders FROM superstore;
-- SELECT 
--     Category,
--     ROUND(SUM(Sales), 2) AS Total_Sales,
--     ROUND(SUM(Profit), 2) AS Total_Profit
-- FROM superstore
-- GROUP BY Category
-- ORDER BY Total_Sales DESC;
-- SELECT 
--     Region,
--     ROUND(SUM(Sales), 2) AS Total_Sales,
--     ROUND(SUM(Profit), 2) AS Total_Profit
-- FROM superstore
-- GROUP BY Region
-- ORDER BY Total_Sales DESC;
-- SELECT 
--     Product_Name,
--     ROUND(SUM(Sales), 2) AS Total_Sales
-- FROM superstore
-- GROUP BY Product_Name
-- ORDER BY Total_Sales DESC
-- LIMIT 10;
-- SELECT 
--     Segment,
--     ROUND(SUM(Sales), 2) AS Total_Sales,
--     ROUND(SUM(Profit), 2) AS Total_Profit
-- FROM superstore
-- GROUP BY Segment
-- ORDER BY Total_Sales DESC;
-- SELECT 
--     State,
--     ROUND(SUM(Sales), 2) AS Total_Sales,
--     ROUND(SUM(Profit), 2) AS Total_Profit
-- FROM superstore
-- GROUP BY State
-- ORDER BY Total_Sales DESC
-- LIMIT 10;
-- SELECT 
--     Discount,
--     ROUND(SUM(Sales), 2) AS Total_Sales,
--     ROUND(SUM(Profit), 2) AS Total_Profit
-- FROM superstore
-- GROUP BY Discount
-- ORDER BY Discount;
-- SELECT 
--     YEAR(STR_TO_DATE(Order_Date, '%m/%d/%Y')) AS Year,
--     ROUND(SUM(Sales), 2) AS Total_Sales,
--     ROUND(SUM(Profit), 2) AS Total_Profit
-- FROM superstore
-- GROUP BY YEAR(STR_TO_DATE(Order_Date, '%m/%d/%Y'))
-- ORDER BY Year;
SELECT 
    Sub_Category,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore
GROUP BY Sub_Category
ORDER BY Total_Sales DESC;



