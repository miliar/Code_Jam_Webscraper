#include<iostream>
#include<fstream>
using namespace std;
ifstream in("tidy.in");
ofstream out("tidy.out");

int check(unsigned long long int n)
{
    while(n>9)
    {
        if(n%10<(n/10)%10)
            return 0;
        n/=10;
    }
    return 1;
}

unsigned long long int solve(unsigned long long int n)
{
    while(!check(n))
        n--;
    return n;
}

int main()
{
    unsigned long long int n;
    int i, cases;
    in>>cases;
    for(i=1;i<=cases;i++)
    {
        in>>n;
        out<<"Case #"<<i<<": "<<solve(n)<<endl;
    }
}
