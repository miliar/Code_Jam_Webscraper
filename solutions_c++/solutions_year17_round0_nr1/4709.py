#include<bits/stdc++.h>
using namespace std;

int compute(string j,int k )
{
    int no_of_flips=0;
    int len=j.length();
    int  p=j.find("-");
    if (p==-1) return 0;
//    cout<<"length of string: "<<len<<"\t"<<"K:"<<"\t"<<k<<" string before manipulation: "<<"\t";
//    for(int i=0;i<len;i++)
//        { cout<<j[i];}



    while(len-p>=k)
    {
//        cout<<"condition :"<<len<<"-"<<1<<"-"<<p<<":"<<len-1-p<<" >= "<<k<<endl;


        if (p==-1) return no_of_flips;

        for(int m=0;m<k && p+m<len ;m++)
        {
              if (j[p+m]=='+') j[p+m]='-' ;
             else j[p+m]='+';


        }
//      cout<<"Position of minus: "<< p<<" new string: "<<j<<endl;
       no_of_flips++;
       p=j.find("-");
    }

//     return -1;


  // int count_minus=count(j.begin(),j.end(),'-');
    //p=j.find("-");
//    cout<<"string after manipuialtion: "<<j;
//        for(int i=0;i<len;i++)
//        { cout<<j[i];}
    //cout<<"\t no of minus: "<<count_minus<<"\t position of first minus: "<<p;
//    cout<<endl;
   //return no_of_flips ;

if (j.find("-")==-1) return no_of_flips;
    else return -1;

}
main()
{
//    freopen("A-small-practice.in","r",stdin);
//    freopen("A-small-practice.out","w",stdout);

    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,k;
    scanf("%d",&t);

    string s;
//    cout<<"printing string"<<endl;
    for (int h=1;h<=t;h++)
    {
       cin>>s>>k;
//
//       cout<<s<<"\t"<<k<<endl;
        int result=compute(s,k);
        if (result==-1) cout<<"Case #"<<h<<": " <<"IMPOSSIBLE";
            //<<" "<<s<<"\t"<<k;
        else cout<<"Case #"<<h<<": "<<result;
        //<<" "<<s<<" "<<"\t"<<k;
         cout<<endl;

    }




}
