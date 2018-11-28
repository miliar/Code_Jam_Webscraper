/**RootAccess IIT Madras*/
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <stack>

using namespace std;

#define INF 1000000007
#define pb push_back
#define rep(a,b) for(i=a;i<b;i++)

int main(int argc, char const *argv[])
{
	int t;
	cin>>t;
	for(int cas=1;cas<=t;cas++)
	{
		int r,c;
		cin>>r>>c;
		vector<vector<char> > mat;

		int minr[26];
		int minc[26];
		int maxc[26];
		int maxr[26];
		int freq[26];
		for(int i=0;i<26;i++)
		{
			minr[i]=26,minc[i]=26;
			maxr[i]=-1,maxc[i]=-1;
			freq[i]=0;
		}
		for(int i=0;i<r;i++)
		{
			vector<char> temp;
			
			for(int j=0;j<c;j++)
			{
				char x;
				cin>>x;
				temp.push_back(x);
				if(x=='?')
					continue;
				//cout<<x<<endl;
				freq[x-'A']++;
				if(minr[x-'A']>i)
					minr[x-'A']=i;
				if(minc[x-'A']>j)
					minc[x-'A']=j;
				if(maxr[x-'A']<i)
					maxr[x-'A']=i;
				if(maxc[x-'A']<j)
					maxc[x-'A']=j;

			}
			mat.push_back(temp);
		}	

		for(int i=0;i<26;i++)
		{
			if(freq[i]==0)
				continue;
			//cout<<(char)('A'+i)<<endl;
			for(int x = minr[i];x<=maxr[i];x++)
			{
				for(int y = minc[i];y<=maxc[i];y++)
					{
						//cout<<x<<" "<<y<<endl;
						mat[x][y]=(i+'A');
						freq[i]++;
					}
			}

		}
		for(int i=0;i<26;i++)
		{
			if(freq[i]==0) continue;
			for(int y= maxc[i]+1;y<c;y++)
			{
				int x;
				for(x = minr[i];x<=maxr[i];x++)
				{
					if(mat[x][y]!='?')
						break;	
				}
				if(x!=maxr[i]+1)
					break;
				for(int x = minr[i];x<=maxr[i];x++)
					mat[x][y]=(char)('A'+i);
				maxc[i]++;
			}
			for(int y= minc[i]-1;y>=0;y--)
			{	int x;
				for(x = minr[i];x<=maxr[i];x++)
				{
					if(mat[x][y]!='?')
						break;	
				}
				if(x!=maxr[i]+1)
					break;
				for(int x = minr[i];x<=maxr[i];x++)
					mat[x][y]=(char)('A'+i);
				minc[i]--;
			}
		}
		
		for(int i=0;i<26;i++)
		{
			if(freq[i]==0) continue;
			for(int x=minr[i]-1;x>=0;x--)
			{	int y;
				for(y=minc[i];y<=maxc[i];y++)
				{
					if(mat[x][y]!='?')
						break;	
				}
				if(y!=maxc[i]+1)
					break;
				for(int y=minc[i];y<=maxc[i];y++)
					mat[x][y]=(char)('A'+i);
				minr[i]--;
			}
			for(int x=maxr[i]+1;x<r;x++)
			{	int y;
				for( y=minc[i];y<=maxc[i];y++)
				{
					if(mat[x][y]!='?')
						break;	
				}
				if(y!=maxc[i]+1)
					break;
				for(int y=minc[i];y<=maxc[i];y++)
					mat[x][y]=(char)('A'+i);
				maxr[i]++;
			}
			/*
			if(freq[c]==1)
			{
				for(int i=minr[i];i>=0;i--)
				{
					if(mat[i][minc[c]]!='?')
						break;
					mat[i][maxc[c]]=(char)(c+'A');
					freq[c]++;
					minr[c]--;
				}
				for(int i=maxr[i];i<r;i++)
				{
					if(mat[i][minc[c]]!='?')
						break;
					mat[i][maxc[c]]=(char)(c+'A');
					freq[c]++;
					maxr[c]++;
				}
				/*
				if(freq[i]>1)
					continue;
				for(int i=minr[c];i>=0;i--)
				{
					if(mat[minr[c]][i]!='?')
						break;
					mat[minr[c]][i]=(char)(c+'A');
					freq[c]++;
					minc[c]--;
				}
				for(int i=minr[c];i>=0;i--)
				{
					if(mat[minr[c]][i]!='?')
						break;
					mat[minr[c]][i]=(char)(c+'A');
					freq[c]++;
					minc[c]--;
				}
				*/
			}
		
		int ans;
		cout<<"Case #"<<cas<<": "<<endl;
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				cout<<mat[i][j];
			}
			cout<<endl;
		}
		
		
		

	}
	return 0;
}