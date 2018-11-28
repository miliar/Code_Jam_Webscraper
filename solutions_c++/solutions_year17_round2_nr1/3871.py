#include <iostream>
#include <algorithm>
#include<iomanip>
#include<fstream>
using namespace std;

int main() {
int t;
ifstream fin;
fin.open("in.txt",ios::in);
ofstream output;
output.open("output.txt",ios::out);
fin>>t;
double d;
int n;

for(int test=0;test<t;test++)
{

fin>>d>>n;


double k[n];
double s[n];
double t[n];

for(int i=0;i<n;i++)
{
fin>>k[i]>>s[i];
double distance=(d-k[i]);
t[i]=distance/s[i];
}

double minPos=*max_element(t,t+n);

double speed =d/(minPos*1.0);
output<<fixed;


output<<"Case #"<<test+1<<": ";
output<<setprecision(6)<<speed<<"\n";

}
return 0;
fin.close();
output.close();

}
