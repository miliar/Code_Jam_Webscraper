#include<iostream>
#include<vector>
#include<cmath>
#include<string>

using namespace std ;
int main()
{

int T ;
cin>>T ;
int data ;
int   dummy ,pivot ;                            //flag for neglection in printing 
vector<int> digit_value ;
vector< string > output ;
for( int j=0 ;j<T ;j++)
{  	 int  flag=0  ;int no_digits=0 ;int counter=0 ;
  string name ;
cin>>name;
// checking for exception 
int dec=0 ;
int temp= name[0]-'0';




pivot=name.size()-1 ;
   for( int i=0 ;i<name.size() ;i++)


{




}


int flag3 =0 ;


 	for( int i=0 ;i<name.size() ;i++)
 	{
 		dummy=name[i]-'0' ;
 		digit_value.push_back(dummy) ;

 		if( i>0 )
 		{  
 			 			if( i !=0 && i!= name.size()-1 )
 			{		

 				if( digit_value[i] == temp)
 				{
 					dec=1 ;
 		

 				
 				}
 				else
 				{
 					dec=0 ;
 					flag3=1 ;
 				}
 			}

 			if( flag==0 && (digit_value[i]< digit_value[i-1] ))
 			{ 
 				pivot=i-1 ;
 				counter=pivot+1 ;
 				digit_value[pivot]=digit_value[pivot]-1 ;
 				
 				flag=1 ;
 				no_digits=name.size() - counter ;

 			}


 		}
 	}



if( dec==1 && (digit_value[name.size()-1] < digit_value[name.size()-2]+1  ) && flag ==1 )
{
	dec=1 ;
}
else if( dec==1 && (digit_value[name.size()-1] == digit_value[name.size()-2] ) && flag ==0 )
{
	dec=0 ;
}
else
{
	dec=0 ;
}
if( flag3 ==1)
{
	dec=0 ;
}

if( dec==0 )
{
int flag2=0 ;
int count=0 ;

// similar part 
for( int i=0 ;i<=pivot ;i++ )
{
	 	if(flag2==0 && digit_value[i]==0 )
	 		{ count++ ;}
	 	else
	 		{ flag2=1 ;}

		name[i]='0'+digit_value[i] ;
}
for( int i=pivot+1 ;i<name.size() ;i++)
{
	name[i]='9' ;
}
name=name.substr( count ,name.size() -count) ;

output.push_back(name) ;
}


if( dec ==1 )
{
 
if( digit_value[0] ==1 )
{   
	string name2 ( name.size()-1 ,'9');
output.push_back(name2) ;

}
else
{  
string name2 ( name.size(),'9');
	name2[0]='0'+(digit_value[0]-1) ;

	output.push_back(name2) ;

}

}

digit_value.clear() ;


}


for( int j=0 ;j<T ;j++)
{
	cout<<"Case #"<<j+1 <<": "<<output[j] <<endl;
}



}