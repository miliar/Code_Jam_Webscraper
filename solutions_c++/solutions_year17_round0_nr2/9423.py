#include <iostream>
#include<vector>
using namespace std;

int main()
{
    int T,d,t=1;
    unsigned long long int N;
    vector <int> v;
    vector <int>::iterator ii;
    vector <int>::reverse_iterator rr;
    cin>>T;
    while(T--)
    {
        v.clear();
        cin>>N;
        while(N)
        {
            d=N%10;
            if(v.size())
            {
                if(d > v.back())
                {
                    for(ii=v.begin(); ii!=v.end(); ii++)
                        (*ii)=9;
                    v.push_back(d-1);

                }
                else v.push_back(d);
            }
            else
            {
                v.push_back(d);
            }
            N/=10;
        }
        cout<<"Case #"<<t++<<": ";
        for(rr=v.rbegin(); rr!=v.rend(); rr++)
            if(*rr)
                cout<<(*rr);
        cout<<endl;
    }
    return 0;
}

