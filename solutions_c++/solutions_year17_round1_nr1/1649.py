#include<iostream>
#include<vector>
#include<map>
#include<queue>
#include<set>
#include<algorithm>
using namespace std;

struct cmp
{
	bool operator() (int A, int B)
	{
		return A < B;
	}
};

int main()
{
	int T,R,C;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		cin>>R>>C;
		vector< vector<char> > V(R, vector<char>(C));
		vector<bool> isEmpty(R);
		for(int m=0;m<R;m++)
		{
			char temp = '?';
			for(int n=0;n<C;n++)
			{
				cin>>V[m][n];
				if(V[m][n] != '?')temp = V[m][n];
				else if (temp != '?')V[m][n] = temp;
			}
			if(temp == '?')isEmpty[m] = true;
			else isEmpty[m] = false;
		}
		for(int m=0;m<R;m++)
		{
			int n = 0;
			while(V[m][n] == '?')n++;
			int x = n-1;
			while(x >=0)
			{
				V[m][x] = V[m][n];
				x--;
			}
		}
		for(int m=0;m<R;m++)
		{
			if(isEmpty[m])
			{
				int x = m;
				while(isEmpty[x] && x < R) x++;
				if(x != R)V[m] = V[x];
				else
				{
					x = m;
					while(isEmpty[x] && x >= 0) x--;
					V[m] = V[x];
				}
			}
		}
		
		cout<<"Case #"<< i << ":\n";
		for(int m=0;m<R;m++)
		{
			for(int n=0;n<C;n++)
			{
				cout<<V[m][n];
			}
			cout<<"\n";
		}
	}
}
