#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
	int t,i=1,j;
	double d,n,k,s;
	double maxi=0;
	cin >> t;
	while(i<=t){
		maxi=0;	
		cin >> d >> n;
		for(j=0;j<n;j++){
			cin >> k >> s;
			if((d-k)/s > maxi) maxi = (d-k)/s;
		}
		cout << fixed << setprecision(6) <<"Case #" << i << ": " << d/maxi << endl;
		i++;
	}
	return 0;
}