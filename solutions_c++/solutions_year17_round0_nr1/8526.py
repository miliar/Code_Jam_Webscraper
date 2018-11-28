#include <iostream>
#include <cstring>
#include <string.h>
#include <vector>
#include <map>
#include <limits>
#include <algorithm>
using namespace std;

int inf = numeric_limits<int>::max();


void construct_value(map<string, int> &value,int n,string s)
{
	if(s.size()==n){
		value[s]=inf;
		return;
	}
	string s1 = s+ "+";
	construct_value(value,n,s1);
	s1=s+"-";
	construct_value(value,n,s1);
	return;
}


bool is_successor(string a,string b,int k)
{
	int n= a.size();
	for (int i = 0; i <= n-k; ++i)
	{
		string s= a;
		for(int j=0;j<k;j++)
		{
			if(s[i+j] == '+'){s[i+j]='-';}
			else{s[i+j]='+';}
		}
		if(b==s){return true;}
	}
	return false;
}

void construct_successor(map<string, int> &value,map<string, vector<string> > &successor,int k)
{
	map<string, int>::iterator it;
	for(it=value.begin();it!=value.end();it++)
	{
		string temp = it->first;
		map<string, int>::iterator it1;
			for (int i = 0; i <= temp.size()-k; ++i)
			{
				string s= temp;
				for(int j=0;j<k;j++)
				{
					if(s[i+j] == '+'){s[i+j]='-';}
					else{s[i+j]='+';}
				}
				successor[temp].push_back(s);
			}
			//cout<<"_______"<<successor[temp].size()<<endl;
	}
}




int main()
{
	int t;
	cin>>t;
	for (int i = 0; i < t; ++i)
	{
		map<string, int> value;
		map<string, vector<string> > successor;
		string s;
		int k;
		int output;
		bool impos = 0;
		cin>>s;
		cin >>k;
		construct_value(value,s.size(),"");
		construct_successor(value,successor,k);
		bool changed=0;
		string end(s.size(),'+');
		//cout<<end;
		value[end]=0;
		while(!changed)
		{
			map<string, int>::iterator it1;
			for(it1=value.begin();it1!=value.end();it1++)
			{
				string temp1 = it1->first;
				//cout<<"STRING:";
				//cout<<temp1<<endl;
				//cout<<"SUCCESSORS:"<<endl;
				if(value[temp1]!=inf)
				{
					vector<string> successors = successor[temp1];
					int n = successors.size();
					//cout<<"n:"<<n<<endl;
					for (int i = 0; i < n; ++i)
					{
						string temp2 = successors[i];
						//cout << temp2;
						if(value[temp2] > value[temp1]+1)
						{
							changed = 1;
							value[temp2] = value[temp1]+1;
						}
					}
					//cout<<"_______________________________________________________"<<endl;
				}
			}
		}
		// for (int j = 0; j < s.size(); ++j)
		// {
		// 	S.push_back(s[j]=='+');
		// }
		if(value[s]==inf)
		{
			impos = 1;
		}
		else
		{
			output = value[s];
		}
		if(impos){cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;}
		else{cout<<"Case #"<<i+1<<": "<<output<<endl;}
	}
}