#include <iostream>


using namespace std;

int main()
{
    int tc;
    cin>>tc;
    for(int y=1; y<=tc; ++y)
    {
        int k,n,iz,der;
        cin>>k;
        cin>>n;
        bool arr[k+2]= {0};
        arr[0]=true;
        arr[k+1]=true;
        for(int j=0; j<n; ++j)
        {
            int ind=0,mayor=0,conta=0;
            for(int i=0; i<k+2; ++i)
            {
                if(arr[i]==false)
                {
                    conta++;

                }
                else
                {
                    if(conta>mayor)
                    {
                        mayor=conta;
                        ind=i;
                    }
                    conta=0;
                }
            }
            //cout<<mayor<<" "<<ind<<endl;
            iz=ind-mayor;
            der=ind-1;
            arr[(der+iz)/2]=true;
            /*for(int t=0; t<k+2; ++t)
            {
                cout<<arr[t];
            }
            cout<<endl;*/
        }
        cout<<"Case #"<<y<<": "<<der-((der+iz)/2)<<" "<<((der+iz)/2)-iz<<endl;
    }

}
