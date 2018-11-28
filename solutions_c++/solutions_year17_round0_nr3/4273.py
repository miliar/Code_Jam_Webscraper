#include <iostream>
#include <map>

using namespace std;

int main()
{

    int t;
    cin>>t;

    for(int i=0;i<t;i++)
    {
        int n,k;
        cin>>n>>k;
        int max1,min1;

        map <int,int,greater<int>> a;
        map<int,int>:: iterator good,bad,bad2;
        a[n]=1;

        for(int j=0;j<k;j++)
        {
            good=a.begin();
            if(((good->first))%2==0)
            {
                bad=a.find((good->first)/2);
                if(bad==a.end())
                {
                    a[(good->first)/2]=1;
                }

                else
                {
                    a[((good->first)/2)]=a[((good->first)/2)]+1;
                }

                bad2=a.find((((good->first)/2)-1));
                if(bad2==a.end())
                {
                    a[(((good->first)/2)-1)]=1;
                }

                else
                {
                    a[(((good->first)/2)-1)]=a[((good->first)/2)-1]+1;
                }

                min1=((good->first)/2)-1;
                max1=(good->first)/2;
            }

            else
            {
                bad=a.find((good->first)/2);
                if(bad==a.end())
                {
                    a[(good->first)/2]=2;
                }

                else
                {
                    a[((good->first)/2)]=a[((good->first)/2)]+2;
                }

                min1=(good->first)/2;
                max1=(good->first)/2;
            }

            (good->second)--;

            if(good->second==0)
                a.erase(good);
        }

        cout<<"Case #"<<i+1<<": "<<max1<<" "<<min1<<endl;
    }




    return 0;
}
