#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <fstream>
#define lli long long int
#define MAX 100
#define li long int
using namespace std;

int c=89;
bool sorting(lli n)
{

    int nextdigii = n%10;
    n = n/10;
    while (n)
    {
        int digii = n%10;
        if (digii > nextdigii)
            return false;
        nextdigii = digii;
        n = n/10;
    }

    return true;
}
int main ()
{
    ifstream input;
    input.open("input1.in");
    ofstream output;
    output.open("output.txt");
    int t;
    input>>t;
    for(int tttt=1;tttt<=t;tttt++)
    {
        lli n;
  input>>n;
   int check=0;
   while(check==0)
   {
       if(sorting(n))
       {
        check=1;
        break;
       }
       else
         n--;
       }
       output<<"Case #" <<tttt<< ": "<<n<<endl;
    }


   return 0;
}
