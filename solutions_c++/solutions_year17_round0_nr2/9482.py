#include <string>
#include <iostream>
using namespace std;

int ch(string &, int );
void nz(string &, int );

int main()
{
	int tce;cin>>tce;
	for(int tc=1;tc<=tce;tc++)
	{
		string s;
		cin>>s;
		int end=s.length()-1;

		int sub=0;
		while (ch(s,end)!=-1)
		{
			if (ch(s,end)!=-1)
			{
				sub=ch(s,end);
				s[sub]--;
				for (int x=sub+1;x<=end;x++)
					s[x]='9';
			}
		}

		nz(s,end);

		cout << "Case #" << tc << ": " << s << endl;

	}

	return 0;
}


int ch(string &str, int e)
{
	for (int j=0;j<e;j++)
	{
		if (str[j]<=str[j+1])
			continue;
		else
			return j;
	}
	return -1;
}

void nz(string &str, int end)
{
	if (str[0]=='0')
	{
		for (int j=1;j<=end;j++)
			str[j-1]=str[j];
		str[end]='\0';
		nz(str,end-1);
	}
}