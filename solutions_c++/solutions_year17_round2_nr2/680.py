#include <iostream>
#include <iomanip>
#include <vector>
#include<string>

using namespace std;



int main()
{
    int tests;
    cin>>tests;
    for (int test=0;test<tests;test++){
        int n;
        cin>>n;
        vector <int> vec,c1;
        for (int i=0;i<6;i++){
            int t;
            cin>>t;
            vec.push_back(t);
        }
        c1=vec;
        string s="ROYGBV";
        string ans="";
        int im=0;
        for (int j=0;j<6;j++)
            if (vec[j]>vec[im])
                im=j;
        ans+=s[im];
        vec[im]--;
        int fim=im;
        for (int i=0;i<n-1;i++){
           int im1=0;
           if (im1==im) im1++;

           if (vec[fim]!=0&&im!=fim){
               im1=fim;
           } else
           for (int j=0;j<6;j++){

               if ((vec[j]>vec[im1]||vec[im1]==0)&&j!=im)
                   im1=j;
           }

            if (vec[im1]==0){
                ans="IMPOSSIBLE";

                break;
            }
//cout<<im1<<" "<<vec[im1]<<" "<<i<<endl;
            im=im1;
            ans+=s[im];
            vec[im]--;
        }
        //cout<<ans<<endl;
        if (ans[ans.length()-1]==ans[0])
            cout<<"Case #"<<(test+1)<<": "<<"IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<(test+1)<<": "<<ans<<endl;



    }




}
