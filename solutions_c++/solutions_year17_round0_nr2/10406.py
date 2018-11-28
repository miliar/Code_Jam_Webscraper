#include<iostream>
#include<fstream>
using namespace std;

bool areSorted(long int n)
{

    int next_digit = n%10;
    n = n/10;
    while (n)
    {
        int digit = n%10;
        if (digit > next_digit)
            return false;
        next_digit = digit;
        n = n/10;
    }

    return true;
}

int main()
{
    freopen("B-small-attempt1.in","r",stdin);
freopen("small_output.txt","w",stdout);
    int t;
    cin>>t;
    for(int j=0;j<t;j++)
    {
        long long tidy;
        long long n;
        cin>>n;

        for(int i=1;i<=n;i++)
        {

            bool a=areSorted(i);
            if(a==true)
            {
                tidy=i;
            }
        }
        cout<<"Case #"<<(j+1)<<": "<<tidy<<endl;
    }
    return(0);
}
