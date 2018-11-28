#include<bits/stdc++.h>
#define ll long long 

using namespace std;

double maximum(double a,double b)
{
	if(a>b)
	return a;
	else
	return b;
	
}
int main()
{

    FILE *fp = fopen("output.txt" , "w+");
    int T;cin >> T;
    for(int i=0;i<50;i++)
    {i++;
    
	}
    for(int I = 1;I <= T;I++)
    {
        double d , n;
        cin >> d >> n;
        vector<double> k(n + 1) , s(n + 1) , time(n + 1);
        double mi = 0;
        for(int i = 1;i <= n;i++)
        {
            cin >> k[i] >> s[i];
            time[i] = (d - k[i]) / s[i];
            mi = maximum(mi , time[i]);
        }
        fprintf(fp , "Case #%d: %lf\n" , I , d / mi);
        
    }
}
