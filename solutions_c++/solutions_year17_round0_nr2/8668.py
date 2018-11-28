#include<cstdio>
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<fstream>

using namespace std;

/*class Tidy_numbers
{
	public:
	void decrease_num(int i,char *data,int len );
	void trim(char *data,int len);
	void solve(ofstream &output,ifstream &fin ,int cn);
};

void Tidy_numbers::decrease_num(int i,char *data_num,int l )
{
	int j=0;
	if(data_num[i]=='0')
	{
		data_num[i]='9';
		data_num[i-1]=data_num[i-1]-1;
	}
	else
	{
		data_num[i]--;
	}
	for(j=l-1;j>i;j--)
	{
		data_num[j]='9';
	}
}

void Tidy_numbers::trim(char *data,int len)
{
int i=0,j=0,mark=0;
if(data[0]=='0')
{
for(i=1;i<=len;i++)
{
	data[i-1]=data[i];
}
}
}

void Tidy_numbers::solve(ofstream &output,ifstream &fin ,int cn)
{
	char data[19];
	int len,i;
	fin>>data;
	len=strlen(data);
	start:
	for(i=len-1;i>0;i--)
	{
		if(data[i-1]>data[i])
		{
			decrease_num(i,&data[0],len);
			goto start;
		}
	}
	trim(&data[0],len);
output<<"Case # "<<(cn+1)<<": "<<data<<"\n";
}


int main()
{
	Tidy_numbers Ti;
	int tc=0,i=0;
	ifstream fin;
    fin.open("input_tidy.in",ios::in);

	ofstream output;
    output.open("output_tidy.txt",ios::out);

	fin>>tc;
	while(i<tc)
	{

		Ti.solve(output,fin,i);
		i++;
	}

fin.close();
output.close();
}
*/

void decrease(int i,char *data,int len )
{int j=0;
	if(data[i]=='0')
	{
		data[i]='9';
		data[i-1]=data[i-1]-1;
	}
	else
	{
		data[i]--;
	}
	for(j=len-1;j>i;j--)
	{
		data[j]='9';
	}
}
void trim(char *data,int len)
{int i=0,j=0,mark=0;
if(data[0]=='0')
{
for(i=1;i<=len;i++)
{
	data[i-1]=data[i];
}


}}
void solve(FILE *fp,FILE *file ,int cn)
{
	char data[19];
	int len,i;
	fscanf(file,"%s",&data);
	len=strlen(data);
	start:
	for(i=len-1;i>0;i--)
	{
		if(data[i-1]>data[i])
		{
			decrease(i,&data[0],len);
			goto start;
		}
	}
	trim(&data[0],len);
fprintf(fp,"Case #%d: %s\n",cn+1,data);
}
main()
{
	int tc=0,i=0;
	FILE* fp = fopen("output_tidy.txt", "w");
	FILE* file = fopen ("B-small-attempt1.in", "r");
	fscanf(file,"%d",&tc);
	while(i<tc)
	{
		solve(fp,file,i);
		i++;
	}
}
