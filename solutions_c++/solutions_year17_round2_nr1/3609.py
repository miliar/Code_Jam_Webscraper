#include <bits/stdc++.h>

using namespace std;

void query(int tc)
{
	cout << setprecision(15);
	vector< pair<double,double> > horses;		
	double d;
	int n;
	cin >> d >> n;
	for (int i=0;i<n;i++)
	{
		double p,sp;
		cin >> p >> sp;
		horses.push_back(make_pair(p,sp));
	}
	sort(horses.begin(),horses.end());	
	double sh_p=horses[n-1].first;
	double sh_sp=horses[n-1].second;
	for (int i=n-2;i>=0;i--)
	{
		double p1=horses[i].first;		
		double sp1=horses[i].second;		
		if (sp1 > sh_sp)
		{			
			double inter=((sh_p-p1)/(sp1-sh_sp))*sp1+p1;	
			if (inter > d)
			{				
				sh_p=p1;
				sh_sp=sp1;
			}
		} else 
		{
			sh_p=p1;
			sh_sp=sp1;
		}
	}	
	double result=d/((d-sh_p)/(sh_sp));
	
	cout << "Case #"<< tc+1 << ": " << result << "\n";
}

int main()
{
	int t;
	cin >> t;
	for (int i=0;i<t;i++) query(i);
	return 0;
}