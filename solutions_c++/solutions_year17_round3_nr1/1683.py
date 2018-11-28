#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <map>
#include <cmath>
#include <climits>
#include <queue>
#include <iomanip>
#include <cstdio>
#define lli long long int
#include<fstream>
#define ll long long
using namespace std;

int main()
{
    ifstream cin("A-large.in");
	ofstream cout("output.txt");
    int t;
    double pi=3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481;
    cin>>t;
    for(int tt=1;tt<=t;tt++){
        cout<<"Case #"<<tt<<": ";

        int n,k;
		cin>>n>>k;
		vector<pair<lli,lli> > inp(n);

		for (int i=0;i<n;i++){
			lli r,h;
			cin>>r>>h;
			inp[i]=make_pair(r,h);
		}

		long long maxar=0;


		for (int i=0;i<n;i++){

			vector<lli> temp;
			long long mb=inp[i].first*inp[i].first+2*inp[i].first*inp[i].second;

			for (int j=0;j<n;j++){

				if (i==j){
					continue;
				}
				ll var=2*inp[j].first*inp[j].second;
				temp.push_back(var);


			}
			sort(temp.begin(),temp.end());
			ll ans=0;
			for (int j=n-2;j>=n-2-k+2;j--){
				ans+=temp[j];
			}
			ans+=mb;



			if (ans>maxar){
				maxar=ans;
			}

		}



		double final=maxar*pi;
		cout << std::fixed;
  		cout << std::setprecision(9) << final<<endl;


    }
}


