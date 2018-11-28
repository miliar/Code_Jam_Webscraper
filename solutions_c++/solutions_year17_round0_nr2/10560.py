#include<iostream>
//#include<conio.h>
#include<dos.h>

using namespace std;


int main()
{
int a,limit[10];
int test,i,temp,cases,j;
//clrscr();

cin>>cases;

for(j=0;j<cases;j++)
{
//cout<<"	case #"<<j+1<<": ";

//delay(1000);
cin>>a;

//test=0; /
for(i=a;i>0;i--)
{
 temp=i;
 test=0;
 while(temp!=0)
 {      //temp=a;
	limit[test]=temp%10;
	temp=temp/10;
	test++;

}
test--         ;
 //limit[test]="\0";
 while(test>=0)
 {
	if(limit[test]<=limit[test-1])
	{     // cout<<limit[test];
	       test--;
//	       delay(10);
		}
	else
	{
	break;
	}
//	test--;

 }
 if(
 test==-1)
 {
// clrscr();

 break;

 }


}


cout<<"	case #"<<j+1<<": "<<i<<endl	;
}
//getch();
return 0;
}//end of the porgram
