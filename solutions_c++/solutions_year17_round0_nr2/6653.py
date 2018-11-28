#include<iostream>
#include<vector>
using namespace std;
bool areSorted(long long int n)
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
    int t;
    vector <int> v;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        long long int n;
        cin>>n;
        while(1)
        {
            bool t=false;
            t=areSorted(n);
            if(t==true)
            {
                v.push_back(n);
                break;

            }

            else
                n--;

        }


    }
     for(int i=0;i<v.size();i++)
    {


            cout<<"case #"<<i+1<<": "<<v.at(i)<<endl;

    }
    return 0;

}

