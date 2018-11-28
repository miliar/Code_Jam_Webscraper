#include <iostream>
#include <vector>
#include <fstream>
#include <stdlib.h>
using namespace std;


int main()
{
ofstream fout("out2.in");
ifstream fin("B-small-attempt1.in");
char ar[1000];
fin.getline(ar,1000);
int t=atoi(ar);
//cin>>t;

for(int i=0;i<t;i++)
{
long long int n;		//the number
fin.getline(ar,1000,'\n');
n=atoi(ar);
//cin>>n;
vector <int> v;		//revers vector
long long int c=n;
while(c>9)
{
v.push_back(c%10);
c=c/10;
}
v.push_back(c);
				// # # # # 3 3

vector<int> r;
for(int s=v.size()-1;s>=0;s--)
{
r.push_back(v[s]);

}
int y=0;





if(r.size()>1)
{
for(int l=1;l<r.size();l++)
{

if(r[l]>=r[l-1])
y++;

}
}



int c1=0;
if(y+1==r.size())
{c1=1;
}


while(c1==0)
{

//cin>>t;
y=0;
c=r.size()-1;
while(r[c]==0 && c!=0)c--;

if(c==0 && r[c]==1)			//if at first place
{
r.pop_back();
for(int l=0;l<r.size();l++)
r[l]=9;//cout<<"1d"<<endl;
}				//




else if(c==0 && r[c]>1)
{
//r.pop_back();
r[0]=r[0]-1;
for(int l=1;l<r.size();l++)
r[l]=9;//cout<<"1d"<<endl;
}

else if(c>0 && c<r.size()-1)
{
r[c]=r[c]-1;
for(int l=c+1;l<r.size();l++)
r[l]=9;//cout<<"1d"<<endl;
}

else if(c==r.size()-1)
{
r[c]=r[c]-1;//cout<<"1d"<<endl;
}




for(int l=1;l<r.size();l++)
{
if(r[l]>=r[l-1])
y++;//cout<<"checking"<<endl;
}
if(y+1==r.size())
c1=1;
//cout<<"c1 is "<<c1<<endl;
}
cout<<"Case #"<<i+1<<": ";
fout<<"Case #"<<i+1<<": ";
for(int l=0;l<r.size();l++){
cout<<r[l];
fout<<r[l];
}
cout<<endl;
fout<<endl;

}


return 0;
}

