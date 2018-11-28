#include <bits/stdc++.h>

using namespace std;




int result;
int AC, AJ;
int N;

pair< pair<int, int> , int > activities[200];		

int Time[2];


void read()
{
	cin>>AC>>AJ;
	N = AC + AJ;
	Time[0] = 0;
	for (int i = 0; i < AC; ++i)
	{
		int a, b;
		cin>>a>>b;
		activities[i] = make_pair( make_pair(a, b), 0);
		Time[0] += b-a;
	}


	Time[1] = 0;
	for (int i = 0; i < AJ; ++i)
	{
		int a, b;
		cin>>a>>b;
		activities[AC + i] = make_pair( make_pair(a, b), 1);
		Time[1] += b-a;
	}
	result = 0;
}


void solve()
{
	sort(activities, activities + N);

//	for (int i = 0; i < N; ++i)
//	{
//		cout<<activities[i].first.first<<" "<<activities[i].first.second<<" "<<activities[i].second<<"\n";
//	}


	vector <int> same[2];
	
	same[1].clear();
	same[0].clear();


	//koniece;

	if(activities[0].second != activities[N-1].second)
		result++;
	else
		same[activities[0].second].push_back(activities[0].first.first + 1440 - activities[N-1].first.second);


	//policz sporne;

	for (int i = 0; i < N-1; ++i)
	{
		if(activities[i].second != activities[i+1].second)
			result++;
		else
		{
			same[activities[i].second].push_back(activities[i+1].first.first - activities[i].first.second);
		//	cout<<activities[i+1].first.second - activities[i].first.first<<"\n";
		}
	}
	sort(same[0].begin(), same[0].end());
	sort(same[1].begin(), same[1].end());

	for (int i = 0; i < same[0].size(); ++i)
	{
		if(Time[0] + same[0][i] > 720)
			result += 2;
		else
			Time[0] += same[0][i];
	}

	//cout<<result<<'\n';
	//cout<<Time[1]<<"\n";
	for (int i = 0; i < same[1].size(); ++i)
	{
	//	cout<<same[1][i]<<"\n";
		if(Time[1] + same[1][i] > 720)
			result += 2;
		else
			Time[1] += same[1][i];
	}



	return;


}






int main(int argc, char const *argv[])
{
	ios_base::sync_with_stdio(0);

	int T;
	cin>>T;
	for (int t = 1; t <= T; ++t)
	{
		read();
		solve();


		cout<<"Case #"<<t<<": "<<result<<"\n";
	}

	return 0;
}