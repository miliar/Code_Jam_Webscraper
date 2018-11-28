#include<iostream>
#include<vector>
#include<map>
#include<queue>
#include<set>
#include<algorithm>
#include<utility>
using namespace std;

	bool cmp (pair<char,int>& A,pair<char,int>& B)
	{
		return A.second >= B.second;
	}

int main()
{
	int T,val,N;
	cin>>T;
	char colors[] = {'R','O','Y','G','B','V'};
	for(int i=1;i<=T;i++)
	{
		cin>>N;
		vector<pair<char,int> > count(6);
		for(int j=0;j<6;j++)
		{
			cin>>val;
			count[j] = make_pair(colors[j],val);
		}
		sort(count.begin(), count.end(), cmp);
		string ans = "";
		while(count[1].second > 0)
		{
			ans+= count[0].first;
			ans+= count[1].first;
			count[0].second--;
			count[1].second--;
		}
		while(count[0].second > 0)
		{
			if(count[2].second <= 0){ans = "IMPOSSIBLE";break;}
			ans+= count[0].first;
			ans+= count[2].first;
			count[0].second--;
			count[2].second--;
		}
		string ans1 = "";
		int len = count[2].second;
		if(len > 0)ans = ans.substr(2*len, string::npos);
		while(count[2].second > 0)
		{
			ans1 += count[0].first;
			ans1 += count[1].first;
			ans1 += count[2].first;
			count[2].second--;
		}
		
		cout<<"Case #"<< i << ": "<< ans1<<ans << "\n";
	}
}
