#include <iostream>
#include <vector>
#include <queue> 
using namespace std;
struct ele 
{
        long long int pos;
        long long int ee;
} ;
class comp
{
public:
	 bool operator()(struct ele a, struct ele b)
	{
		if( a.ee < b.ee)
		    return true;
		 else
		       return false;// lesser than for max heap
		}
};
int main()
 {
	long long int n,i,s,myint,j,e,p,cnt,lastl,lastr,ls,rs,f,g=1;
	vector<long long int> myvector;
	priority_queue<struct ele, vector<struct ele>, comp> q;
        cin>>n;
        for(i=0;i<n;i++)
  	  {
               cin>>s;
               struct ele h;
               struct ele t;
               struct ele y;
               h.ee=s;
               h.pos=0;
               q.push(h);
               s=s+2;
               for(j=0;j<s;j++)
               {
                   myvector.push_back(0);
               }
               myvector.at(0)=1;
               myvector.at(s-1)=1;
            cin>>e;
               for(j=0;j<e;j++)
               {
                    h=q.top();
                    q.pop();
           if(h.ee%2==0)
                    {
                         p=h.ee/2;
                         myvector.at(p+h.pos)=1;
                         lastl=p+h.pos;
               lastr=p+h.pos;
               t.pos=p+h.pos;
                         y.pos=h.pos;
                         y.ee=t.pos-y.pos-1;
        cnt=0;f=1;
                 while(1)
                         {
             //                cout<<"while1"<<myvector.at(t.pos+1)<<"\n";
                              if(myvector.at(t.pos+f)==1)
          	                    break;
                    else
                    {
                        cnt++;f++;
                    }
        	          }	
 		               t.ee=cnt;
               q.push(t);
		               q.push(y);
		       }
    		       else
  	               {
		              p=h.ee/2+1;
		               myvector.at(p+h.pos)=1;
               lastl=p+h.pos;
               lastr=p+h.pos;
		               t.pos=p+h.pos;
               y.pos=h.pos;
               y.ee=t.pos-y.pos-1;
               cnt=0;f=1;
		               while(1)
		               {
		       //            cout<<"while2"<<"\n";
                   if(myvector.at(t.pos+f)==1)
                	        break;
                   else
                   {f++;
                        cnt++;}
		               }
		               t.ee=cnt;
               q.push(t);
		               q.push(y);
		        }
       
           }
            ls=0;rs=0;
        while(1)
		          {
		   //           cout<<"while3"<<"\n";
              if(myvector.at(lastl-1)==1)
		                    break;
		              else
		                {
                    lastl--;
		                   ls++;
                		}
           }
           		  while(1)
		           {
		 //              cout<<"while4"<<"\n";
              if(myvector.at(lastr+1)==1)
		                    break;
		              else
		                {
		                    lastr++;
                    rs++;
		                }
           }
		          if(rs>ls)
           {
               cout<<"Case #"<<g<<": "<<rs<<" "<<ls<<"\n";g++;
           }
           else
		           {
               cout<<"Case #"<<g<<": "<<ls<<" "<<rs<<"\n";g++;
           }
            while (!myvector.empty())
  {
    
     myvector.pop_back();
  }while (!q.empty())
  {
    
     q.pop();
  }
    }
	return 0;
}
