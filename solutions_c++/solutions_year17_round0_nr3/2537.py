#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <queue>
#include <functional>
#include <list>
#include <set>
#include <sstream>
#define ll long long
#define INF 1000000007

using namespace std;

priority_queue<pair<ll,ll>> Q;

int main()
{
	ios::sync_with_stdio(false);

	//while(cin>>n)

	int T;
	cin>>T;
	for(int cas=1;cas<=T;cas++)
	{
		ll n,k,mx,mi;
		cin>>n>>k;

		while(!Q.empty())Q.pop();
		Q.push(make_pair(n,1));
		while(!Q.empty())
		{
			auto x = Q.top();
			Q.pop();
			while(!Q.empty()&&Q.top().first == x.first){
				x.second += Q.top().second;
				Q.pop();
			}

			ll len = x.first, num = x.second;
			//cout<<len<<' '<<num<<' '<<k<<endl;
			len--;

			if(k>num){
				k -= num;
				Q.push(make_pair(len/2,num));
				Q.push(make_pair(len-len/2,num));
			}
			else
			{

				mx = len/2;
				mi = len-len/2;
				if(mi>mx)swap(mi,mx);
				break;
			}
		}

		cout<<"Case #"<<cas<<": "<<mx<<' '<<mi<<endl;
		//cout<<"Case "<<cas<<": ";
	}

	return 0;
}
