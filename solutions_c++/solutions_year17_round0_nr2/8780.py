#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin("B-small-attempt0.in");
    ofstream fout("outfile.out");
int t; fin>>t;
for(int k=1;k<=t;k++)
{
    int ind=0, count=0;
	string num;fin>>num;
	if(num.size()==1)
    {
        fout<<"Case #"<<k<<": "<<num<<endl;
        continue;
    }
    int f(0),c(0);
    for(int i=0;i<num.size()-1;i++)
    {
        if(num[i]!=num[i+1])
            f=1;
        if(num[i]>num[i+1])
            c=1;
    }
    if(f == 0)
        fout<<"Case #"<<k<<": "<<num<<endl;
    else if(c==0)
        fout<<"Case #"<<k<<": "<<num<<endl;
    else{
	for(int i=0; i<num.size()-1;i++)
	{
		if(num[i+1]<= num[i] && count==0) //132
			{
				num[i] = num[i]-1;
				num[i+1]='9';
				count++;
			}
        if(num[i+1]<= num[i] && count!=0)
        {
            num[i+1]='9';
            count++;
        }
    }
    fout<<"Case #"<<k<<": ";
    int flag = 0;
    for(int i=0;i<num.size();i++)
    {
        if(num[i]=='0' && flag ==0)
            continue;
        else if(num[i]=='1')
        {
            fout<<num[i];
            flag = 1;
        }
        else
            fout<<num[i];
    }
    fout<<endl;
    }
}

fin.close();
fout.close();
return 0;
}
