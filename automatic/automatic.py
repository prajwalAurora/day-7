# ----------------- Automatic Observation -----------------
def generate_observation(forecast_df):
    obs = ""
    avg_units = forecast_df["Units_Sold"].mean()
    max_units = forecast_df["Units_Sold"].max()
    max_day = forecast_df.loc[forecast_df["Units_Sold"].idxmax(), "Date"].strftime("%Y-%m-%d")
    
    avg_revenue = forecast_df["Revenue"].mean()
    max_revenue = forecast_df["Revenue"].max()
    max_rev_day = forecast_df.loc[forecast_df["Revenue"].idxmax(), "Date"].strftime("%Y-%m-%d")
    
    if forecast_df["Units_Sold"].iloc[-1] > forecast_df["Units_Sold"].iloc[0]:
        obs += "Forecast shows an increasing demand trend.\n"
    else:
        obs += "Forecast shows a decreasing/stable demand trend.\n"
        
    obs += f"Peak units ({int(max_units)}) expected on {max_day}.\n"
    obs += f"Peak revenue (₹{max_revenue:.2f}) expected on {max_rev_day}.\n"
    obs += f"Average daily units: {int(avg_units)}, average daily revenue: ₹{avg_revenue:.2f}\n"
    
    if "Holiday" in forecast_df.columns:
        if forecast_df["Holiday"].sum() > 0:
            obs += f"{int(forecast_df['Holiday'].sum())} holiday days may affect demand.\n"
    
    return obs