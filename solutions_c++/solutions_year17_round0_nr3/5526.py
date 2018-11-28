#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int a=1;a<=t;a++)
    {
        int n,k;
        cin>>n>>k;
        vector<int>data;
        data.push_back(0);
        data.push_back(n+1);
        int arr[n+1];
        int count=1;
        int max=data[1]-data[0]-1;
        int flag=1;
        while(flag)
        {
            for(int b=0;b<data.size()-1;b++)
            {
//                cout<<"data \n";
//                for(int a=0;a<data.size();a++)
//                    cout<<data[a]<<" ";
//                cout<<endl;
//                cout<<"max is "<<max<<endl;
                if((data[b+1]-data[b])-1>=max)
                {
                    arr[(data[b+1]+data[b])/2]=count++;
                    data.insert(data.begin()+b+1,(data[b+1]+data[b])/2);
                    b++;
                    if(data.size()==k+2)
                    {
                        if(data[b]-data[b-1]<=data[b+1]-data[b])
                        cout<<"Case #"<<a<<": "<<data[b+1]-data[b]-1<<" "<<data[b]-data[b-1]-1<<endl;
                        else
                        cout<<"Case #"<<a<<": "<<data[b]-data[b-1]-1<<" "<<data[b+1]-data[b]-1<<endl;
                        flag=0;
                        break;
                    }
                }
            }
            max=data[1]-data[0]-1;
            for(int x=1;x<data.size();x++)
                if(data[x]-data[x-1]-1>max)
                    max=data[x]-data[x-1]-1;

        }
//        for(int a=1;a<n+1;a++)
//            cout<<arr[a]<<" ";
//        cout<<"\n";
    }
}
