#include<bits/stdc++.h>
#define ll long long
using namespace std;

main()
{
    int t;
    cin>>t;
    int T = t;
    for(int j = 1;j<=t;  j++)
    {
        ll n;
        cin>>n;
       // cout<<"\n\n\n";
        
        if((n / 10) == 0)
           cout<<"Case #"<<j<<": "<<n<<"\n";
        else
        {
            ll N = n;
            
            int count = log10(n) + 1;
            
            int arr[count];
            
         //   cout<<" c "<<count;
            
            for(int i = count-1; i>=0; i--)
            {
                arr[i] = n%10;
                n = n/10;
            }   
            
            int i = 0;
            
           // for(int k=0; k<count; k++)
           //    cout<<"   "<<arr[k];
            
            while(arr[i] <= arr[i+1] && i<count-1)
               i++;
            
            if((i == count-1) && (arr[i-1] <= arr[i]))
               {
                   cout<<"Case #"<<j<<": "<<N<<"\n";
                //cout<<"a";
               }
            else
            {
             //   cout<<" i "<<i;   
            
                int p = count - i -1;
                
                int t = p;
            
                n = N;
                
           //     cout<<"  N  "<<n;
                
                while(i>1 &&  arr[i-1] == arr[i])
                {
                    p++;
                    i--;
                }   
            
               if(i == 1 && arr[0] == arr[1]) p++;
            
               // cout<<" p "<<p;
            
                n = n / pow(10,p);
            
           //     cout<<" n "<<n;
            
                n = n * pow(10,p);
                
                cout<<"Case #"<<j<<": "<<n-1<<"\n";
            }    
        }   
           
           
    }
}
