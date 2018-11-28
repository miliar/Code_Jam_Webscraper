#include <cstdio>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

void alphabat(vector<vector<int> >& pos,vector<string>& result, int R,int C)
{
	int r = 0;
	while(r<R)
	{
		if(pos[r].size()==0) 
		{
			r++;
			continue;
		}
		for(int c:pos[r])
		{
			int left = c-1, right = c+1;
			while(left>=0 && result[r][left]=='?')
				result[r][left--] = result[r][c];
			while(right<C && result[r][right]=='?')
				result[r][right++] = result[r][c];
		}
		int up = r-1, down = r+1;
		while(up>=0 && pos[up].size()==0)
			result[up--] = result[r];
		while(down<R && pos[down].size()==0)
			result[down++] = result[r];
		r = down;
	}
}

int main()
{
	int t, R, C;
	string row;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>R>>C;
		vector<vector<int> > pos;
		vector<string> result;
		for(int r=0;r<R;r++)
		{
			pos.push_back(vector<int>());
			cin>>row;
			result.push_back(row);
			for(int c=0;c<C;c++)
				if(row[c]!='?')
					pos.back().push_back(c);
		}
		alphabat(pos,result,R,C);
		cout<<"Case #"+to_string(i+1)+":"<<endl;
		for(int r=0;r<R;r++)
			cout<<result[r]<<endl;
	}
	return 0;
}

