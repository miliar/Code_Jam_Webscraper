#include <iostream>
#include <vector>
using namespace std;
int main(int argc, char const *argv[])
{
	int t;
	cin>>t;
	for(int f=1;f<=t;f++)
	{
		int r,c;
		cin>>r>>c;
		vector<string> v;
		for(int i=0;i<r;i++)
		{
			string s;
			cin>>s;
			v.push_back(s);
		}
		for(int i=0;i<v.size();i++)
		{
			char temp='?';
			for(int j=0;j<v[i].length();j++)
			{
				if(v[i][j]!='?'){
					temp = v[i][j];
					break;
				}
			}
			if(temp=='?'){
				if(i!=0)
					v[i] = v[i-1]; 
			}
			else{
				for(int j=0;j<v[i].length();j++){
					if(v[i][j]=='?')
						v[i][j] = temp;
					else
						temp = v[i][j] ;
					//if(i!=0&& v[i-1][j]=='?'){
						int rowch = i-1;
						while(rowch>=0 && v[rowch][j]=='?'){
							v[rowch][j] = temp;
							rowch--;

					//	}
					}
				}
			}
		}
		cout<<"Case #"<<f<<":"<<endl;
		for(int i=0;i<v.size();i++){
			cout<<v[i]<<endl;
		}
	}
	return 0;
}