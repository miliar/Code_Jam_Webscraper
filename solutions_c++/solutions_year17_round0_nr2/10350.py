#include<iostream>
#include<fstream>
#include<malloc.h>
using namespace std;

int main()
{
    ifstream fin;
    fin.open("/home/kiit/Downloads/B-small-attempt0.in");   ///Input file.
    ofstream fout;
    fout.open("/home/kiit/out2.txt");
    int t;
    fin>>t; ///The number of test cases.
    int n;
    int c;
    int p = 1;
    while(fin>>n)
    {
        if(n/10==0)
        {
            fout<<"Case #"<<p<<": "<<n<<endl;
            p++;
            continue;   ///The whole code snippet following the this statement is skipped.
        }
        ///This  is the case if 'N' is a two digit number.
        int m = 9;
        for(int i=10;i<=n;i++)
        {

            c = 0;
            int *d = (int *)malloc(1*sizeof(int));
            int a = i;
            int rem = a % 10;
            d[0] = rem;
            a /= 10;
            c = 1;
            while(a>0)
            {
                rem = a % 10;
                d = (int *)realloc(d,(c+1)*sizeof(int));
                d[c] = rem;
                a = a / 10;
                c++;
            }
            int flag = 0;
            for(int k=0;k<=c;k++)
            {
                if(d[k]<d[k+1] && (k+1)<c)
                {
                    flag = 1;
                    break;
                }
            }
            if(flag==0)
                m = i;
        }
        fout<<"Case #"<<p<<": "<<m<<endl;
        p++;
    }
    fin.close();
    return 0;
}
