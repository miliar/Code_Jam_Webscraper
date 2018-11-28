#include<iostream>


using namespace std;
int test,N,testno,out,y;
void tidy(int ,int& );
int main()
{
 cin>>test;
 if(test<1||test>100)
  goto end;
  
  testno=1; 

 while(test) 
   { cin>>N; 
    if(N<1 || N>1000)          
       goto end;
      
     if(N>=1 && N<10)
       cout<<"Case"<<" "<<"#"<<testno<<":"<<" "<<N<<"\n";
     
     else
      {tidy(N,y);
      cout<<"Case"<<" "<<"#"<<testno<<":"<<" "<<y<<"\n";}
      
     testno++;
     test--;} 
     
    
    
    end:return 0;        
    }
    

    
 
void tidy(int num,int &y )
  {  int i=0,p=0,len=0,q=0;
     int arr[100];
     int N=num;
     //cout<<"N"<<N<<"\n";
     //clear arry
     for(int i=0;i<100;i++)
     arr[i]=0;
     
     while(num!=0 )
     {int a=num%10;
      num=num/10;
      arr[i]=a;
      i++;}
      len=i; 
     // cout<<"len"<<len<<"\n"; 
      
     for(i=0;i<len-1;i++)if(arr[i]>arr[i+1]||arr[i]==arr[i+1])p++;
     if(p==len-1)
     y=N;
     else
     tidy(N-1,y); 
     
      
      
      }
      
 
 
       
