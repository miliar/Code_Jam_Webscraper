#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    long long int n,temp;int ans=0;
    int arr[200];
  freopen("input.in","r",stdin);
   freopen("output.txt","w",stdout);
    cin>>t;
    for(int q=1;q<=t;q++)
    {   ans=0;
        cin>>n;
        cout<<"Case #"<<q<<": ";
        temp=n;
        int i=0;
        while(temp!=0)
        {
            arr[i++]=temp%10;
            temp=temp/10;
        }
        bool flag=true;
        for(int j=0;j<i-1;j++)
        {
            if(arr[j]>=arr[j+1])
                continue;
            else { temp=j;
                   flag=false;
                    break;
                }
        }
        if(flag) cout<<n<<endl;
        else
        {  for(int j=0;j<temp;j++)
                arr[j]=9;
           for(int j=temp;j<i-1;j++)
            {
                if(arr[j]<arr[j+1])
                {   flag=true;
                    arr[j]=9;
                   if( arr[j+1] > 1) arr[j+1]=arr[j+1]-1;
                   else {   arr[j+1]=9;
                            j+=2;
                            if(j==i) ans=-1;
                            else{
                            while(arr[j]<=1 && j<i)
                            {   arr[j]=9;
                                j++;
                                if(j==i)
                                {
                                  ans=-1;break;
                                }
                            }
                            if(ans!=-1)
                            arr[j]-=1;
                            j--;}
                        }
                   for(int k=j+1;k<i-1;k++)
                   {
                       if(arr[k]>=arr[k+1])
                           {
                               continue;
                           }
                       else{
                            flag=false;
                            //arr[j+1]+=1;
                            break;
                           }
                   }

                }
                else arr[j]=9;
                if(flag) break;

            }

            if(ans == -1)
            {
                for(int k=0;k<i-1;k++)
                    cout<<"9";
                cout<<endl;
            }
            else
            {
                for(int k=i-1;k>=0;k--)
                    cout<<arr[k];
                cout<<endl;
            }

        }

    }

    fclose(stdin);
    fclose(stdout);

    return 0;

}
