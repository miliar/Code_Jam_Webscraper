#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>
#define SIZE 20

using namespace std;

char str[SIZE];

string getmax(string A,string B)
{
	if(A.size()<B.size()) return B;
	if(A.size()>B.size()) return A;
	return max(A,B);
}
int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		scanf("%s",&str);
		int n=strlen(str);
		string ret="1";
		if(n>=2)
		{
			string cand="";
			for(int i=0;i<n-1;i++) cand+="9";
			ret=getmax(ret,cand);
		}
		int pos=0;
		while(pos+1<n&&str[pos]<=str[pos+1]) pos++;
		if(pos==n-1)
		{
			string S=str;
			ret=getmax(ret,S);
		}
		else
		{
			while(pos>0&&str[pos]==str[pos-1]) pos--;
			//printf("%d\n",pos);
			if(str[pos]>'1')
			{
				string S="";
				for(int i=0;i<pos;i++) S+=str[i];
				S+=(str[pos]-1);
				for(int i=pos+1;i<n;i++) S+="9";
				ret=getmax(ret,S);
				//printf("%s\n",S.c_str());
			}
		}
		printf("%s\n",ret.c_str());
	}
	return 0;
}
