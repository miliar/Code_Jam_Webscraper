#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    ofstream file;
    ifstream input;
    file.open("B-output.txt");
    input.open("B-small-attempt0.in");
    input>>t;
    int n=1;
    while(n<=t)
    {
        int num;
        input>>num;
        for(int i=num;i>=1;i--)
        {
            int x=i,counter=0,c=0;
            while(x>0)
            {
                c++;
               int a,b;
               a=x%10;
               x=x/10;
               b=x%10;
               if(a>=b)
                counter++;
            }
            if(counter==c)
            {
                file<<"Case #"<<n<<": "<<i<<endl;
               i=0;
            }
        }
        n++;
    }
    return 0;
}
