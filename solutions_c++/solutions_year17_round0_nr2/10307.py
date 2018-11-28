#include<iostream>
#include<fstream>
using namespace std;

long findTidy(long n)
{
    long copy1N = n;
    long count = 0;
    while(copy1N != 0)
    {
        copy1N /= 10;
        count++;
    }
    long copy2N = n;
    long needToReduce = 0;
    long a[count];

    for (long i = count-1; i >= 0; i--) {
        a[i] = copy2N % 10;
        copy2N /= 10;
    }

    for(long i=0;i<count-1;i++)
    {
        if(a[i]>a[i+1])
        {
            needToReduce = 1;
            break;
        }

    }
    /*
    for(long i=0;i<count;i++)
    {
        cout<<a[i]<<",";
    }
    cout<<"\n";
    */
    if(needToReduce == 1)
        return findTidy(n-1);
    else
        return n;
}



int main()
{
   // freopen("b-small.in","r",stdin);
   // freopen("output.out","w",stdout);
   ifstream input("b-small2.in");
   ofstream output("b-small2.out");
   /* double test;
    cin>>test;
    for(int i=1;i<=test;i++){
        long n;
        input >> n;
        cout<<"Case #"<<i<<": "<<findTidy(n);
        cout<<"\n";
    }
    */

    long n;
    int c = 1;
    while(input >> n)
    {
        if(c==1){
            c++;
            continue;
        }
        output<<"Case #"<<c-1<<": "<<findTidy(n)<<"\n";
        c++;
    }
    return 0;
}
