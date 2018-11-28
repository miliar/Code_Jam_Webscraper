#include <bits/stdc++.h>

using namespace std;


struct comparator{
	bool operator() (const pair<long long, long long> &a, const pair<long long, long long> &b) const{
		if (a.first == b.first)
			return a.second > b.second;
		return a.first > b.first;
	}

};


multiset <pair<long long, long long>, comparator> odcinki;

long long n,k;



void read()
{
	cin>>n>>k;
	k--;
	odcinki.clear();
	odcinki.insert(make_pair(n,1));
	return;
}

void solve()
{
	while(k>0)
	{
		auto top = *odcinki.begin();
		
		odcinki.erase(odcinki.begin());

		//cout<<k<<" "<<top.first<<" "<<top.second<<"\n";

		if(top.second <=k )
		{
			if(top.first % 2)
			{
				odcinki.insert(make_pair( top.first/2, top.second*2 ));
				k -= top.second;
			}
			else
			{
				odcinki.insert(make_pair( top.first/2,    top.second ));
				odcinki.insert(make_pair( top.first/2 -1, top.second ));
				k -= top.second;
			}
		}
		else
		{
			if(k % 2)
			{
				odcinki.insert(make_pair( top.first/2, k*2 ));
				odcinki.insert(make_pair( top.first , top.second-k ));
				
				k = 0;
			}
			else
			{
				odcinki.insert(make_pair( top.first , top.second-k ));
				odcinki.insert(make_pair( top.first/2,    k ));
				odcinki.insert(make_pair( top.first/2 -1, k ));
				k = 0;
			}	
		}
	}


//	cout<<k<<" "<<odcinki.begin()->first<<" "<<odcinki.begin()->second<<"\n";

	if(odcinki.begin()->first == 0)
		cout<<"0 0";
	else
		if(odcinki.begin()->first % 2)
			cout << odcinki.begin()->first / 2 <<" "<<odcinki.begin()->first / 2;
		else
			cout << odcinki.begin()->first / 2 <<" "<<odcinki.begin()->first / 2 -1;
	return;
}



int main(int argc, char const *argv[])
{
	ios_base::sync_with_stdio(0);

	int T;


	cin>>T;
	for(int t=1; t <= T; ++t)
	{
		read();
		cout<<"Case #"<<t<<": ";
		solve();
		cout<<"\n";

	}


	return 0;
}