#include<fstream>
#include<string>

using namespace std;

char flip(char a)
{
	if(a=='-')
		return '+';
	return '-';
}

/*int flip(string str, int i, int j, int k)
{
	int move=0;
	int cur=i;
	while(cur<=j){
		int it=0,next=-1;
		if(str[cur]=='-')
			str[cur]='+';
		else
		{
			str[cur]='-';
			if(next==-1)
				next=cur;
		}
		it++;
		cur++;
		if(it==k)
		{
			cur=next;
			move++;
		}
		if(next==-1)
			break;
	}
	return move;
}*/


int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	int t;
	fin>>t;
	for(int ca=1; ca<=t; ca++)
	{
		string str;
		fin>>str;
		int k;
		fin>>k;
		bool pos=true;
		int move=0;
		int len=str.length();
		//fout<<str<<" "<<k<<"\n";
		/*while(i<len && str[i]=='+')
			i++;
		if(i<len)
		{
			while(i<len)
			{
				while(i<len && str[i]=='+')
					i++;
				if(i==len)
					break;
				int p=i;
				while(i<len && str[i]=='-')
					i++;
				int curlen=i-p;
				move += (curlen/k);
				p=i;
				i= i-(curlen%k);
				if(i==len)
					break;
				while(p<len && str[p]=='+')
					p++;
				if(p==len && curlen%k!=0){
					pos=false;
					break;
				}
				int pl=curlen%k;
				int rl=k-pl;
				int cl=0;
				while(p<len && cl<rl && str[p]=='-')
				{
					cl++;
					p++;
				}
				if(cl<rl)
				{
					pos=false;
					break;
				}
				int j=p-1;
				move += flip(str,i,j,k);
				i=p;
			}
		}*/
		for(int i=0; i<len; i++)
		{
			if(str[i]=='+')
				continue;
			if(len-i < k)
			{
				pos=false;
				break;
			}
			for(int j=i; j<i+k; j++)
				str[j]=flip(str[j]);
			move++;
		}
		fout<<"Case #"<<ca<<": ";
		if(pos)
			fout<<move<<"\n";
		else
			fout<<"IMPOSSIBLE\n";
	}
}