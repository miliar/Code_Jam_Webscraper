#include<fstream>
#include<string>
#include<queue>
#include<unordered_map>
using namespace std;
char change(char in)
{
	if(in=='+')
		return '-';
	return '+';
}
int main()
{
	ifstream cin("A-small-attempt0.in");
	ofstream cout("output.txt");
	int num;
	cin>>num;
	int siz;
	string str,temp,tar;
	pair<string,int> p;
	bool done=false;
	for(int a=1;a<=num;a++)
	{
		queue<pair<string,int>> q;
		unordered_map<string,bool> um;
		cin>>str>>siz;
		q.push(make_pair(str,0));
		tar.clear();
		for(int i=1;i<=str.size();i++)
			tar.push_back('+');
		if(str==tar)
		{
			cout<<"Case #"<<a<<": 0\n";
			continue;
		}
		done=false;
		while(!q.empty())
		{
			p=q.front();
			for(int i=0;i<str.size()-siz+1;i++)
			{
				temp=p.first;
				for(int j=i;j<siz+i;j++)
				{
					temp[j]=change(temp[j]);
				}
				if(temp==tar)
				{
					cout<<"Case #"<<a<<": "<<p.second+1<<"\n";
					done=true;
					break;
				}
				try
				{
					um.at(temp);
				}
				catch(...)
				{
					q.push(make_pair(temp,p.second+1));
					um[temp]=false;
				}
			}
			if(done)
				break;
			q.pop();
		}
		if(done)
			continue;
		cout<<"Case #"<<a<<": IMPOSSIBLE\n";
	}
}
