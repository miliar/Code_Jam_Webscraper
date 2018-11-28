#include <bits/stdc++.h>
using namespace std;

char a[12][12];
int r,c;

vector<char> huruf;
int lr[200],lc[200];
int cnt[200];
bool found=false;
void solve(int x, int y)
{
	if(found)	return;
	if(x==r)
	{
		/*
		for(int temp=0;temp<r;temp++)
			{
				for(int temp2=0;temp2<c;temp2++)
				{
					cout<<a[temp][temp2];
				}
				cout<<"\n";
			}
		cout<<"\n";*/
		bool visited[200];
		memset(visited,false,sizeof(visited));
		int temp,temp2,temp3,temp4;
		bool check=true;
		for(temp=0;(temp<r) && (check);temp++)
		{
			for(temp2=0;(temp2<c)&& (check);temp2++)
			{
				int cur=a[temp][temp2];
				if(visited[cur])	continue;
				visited[cur]=true;
				//cout<<char(cur)<<" "<<lr[cur]<<" "<<lc[cur]<<"\n";
				if((lr[cur]-temp+1)*(lc[cur]-temp2+1)!=cnt[cur])	check=false;
				for(temp3=temp;(temp3<=lr[cur]) && (check);temp3++)
				{
					for(temp4=temp2;(temp4<=lc[cur]) && (check);temp4++)
					{
						if(a[temp3][temp4]!=cur)	{check=false;
						break;
						}
					}
				}
			}
		}
		if(check)
		{
			found=true;
			for(temp=0;temp<r;temp++)
			{
				for(temp2=0;temp2<c;temp2++)
				{
					cout<<a[temp][temp2];
				}
				cout<<"\n";
			}
		}
	}
	else
	{
		if(isalpha(a[x][y]))
		{
			cnt[a[x][y]]++;
			int sr=lr[a[x][y]],sc=lc[a[x][y]];
			lr[a[x][y]]=x; lc[a[x][y]]=y;
			if(y!=c-1)	solve(x,y+1);
			else	solve(x+1,0);
			cnt[a[x][y]]--;
			lr[a[x][y]]=sr; lc[a[x][y]]=sc;
		}
		else
		{
			int temp;
			
			for(temp=0;temp<huruf.size();temp++)
			{
				int next=huruf[temp];
				int sr=lr[next],sc=lc[next];
				lr[next]=x; lc[next]=y;
				a[x][y]=char(next);
				//cout<<a[x][y]<<" "<<x<<" "<<y<<"\n";
				cnt[next]++;
				if(y!=c-1)	solve(x,y+1);
				else	solve(x+1,0);
				cnt[next]--;
				lr[next]=sr; lc[next]=sc;
				a[x][y]='?';
			}
		}
	}
}

int main()
{
	freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
	int tc;
	cin>>tc;
	for(int tmp=1;tmp<=tc;tmp++)
	{
		int temp,temp2;
		cin>>r>>c;
		found=false;
		huruf.clear();
		for(temp=0;temp<r;temp++)
		{
			for(temp2=0;temp2<c;temp2++)
			{
				//cout<<temp<<" "<<temp2<<"\n";
				cin>>a[temp][temp2];
				if(isalpha(a[temp][temp2]))	huruf.push_back(a[temp][temp2]);
				
			}
		}
		//for(temp=0;temp<huruf.size();temp++)	cout<<huruf[temp];
		printf("Case #%d:\n",tmp);
		solve(0,0);
		
	}
}
