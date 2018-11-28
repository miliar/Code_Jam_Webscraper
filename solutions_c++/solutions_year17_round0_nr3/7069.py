#include<iostream>
#include<vector>
#include<algorithm>
 using namespace std;

 int main()
 {
     int T,l=1;
     long long int N, K,gap,inserted,n1,n2,pos,check;;
     vector<long long int> occ;
     vector<long long int>::iterator i;
     cin>>T;

     while(l<=T)
     {
         cin>>N>>K;
         gap=-1;
         occ.push_back(1);
         //cout<<"occ.push_back(1) "<< occ[0]<<endl;
         occ.push_back(N+2);
         //cout<<"occ.push_back(N+2) "<< occ[1]<<endl;

         while(K--)
         {
             for(i=occ.begin();i<occ.end()-1;i++)
             {
                 check=*(i+1)-*i-1;
                 //cout<<check<<endl;
                 if( check > gap )
                    {
                        gap=check;;
                        pos=*i;
                    }
             }
             //cout<<"for k="<<K<<", gap="<<gap<<", pos="<<pos<<endl;
                    if(gap%2==0)
                        inserted=pos+gap/2;
                    else
                        inserted=pos+gap/2+1;
                //cout<<"inserted at : "<<inserted<<endl;
               for(i=occ.begin();i<occ.end();i++)
                {
                if(*i > inserted){
                    occ.insert(i,inserted);
                    break;}
                }

             if(K==0){
             for(i=occ.begin();i<occ.end();i++)
                {
                    if(*i==inserted){
                        n1=  *i-*(i-1)-1;
                        n2= *(i+1) - *i -1;}
                }
             }
             gap=-1;
        }//end of k

        cout<<"Case #"<<l<<": "<<max(n1,n2)<<" "<<min(n1,n2)<<endl;

        l++;
        occ.clear();

    }//end of test cases


     return 0;
 }
