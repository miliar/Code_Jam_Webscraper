#include <iostream>
#include <sstream>
#include<cstdio>
using namespace std;
/*

public static boolean isAscending (String digits) {
    for (int i = 1; i < digits.length (); ++i)
        if (digits.charAt (i-1) > digits.charAt (i)) 
            return false;
    return true;
}

public static void count (int base, int size)
{    
    double max = Math.pow (base, size);
    for (int i = 0; i < max; ++i)
    {
        String res = Integer.toString (i, base);
        if (isAscending (res.replaceAll ("0", "")))
            System.out.printf ("%0"+size+"d ", Long.parseLong (res)); 
    }
}


*/

string int_to_str(int num)
{
    stringstream ss;
    ss << num;
    return ss.str();
}
bool isAscending(string digits){
	for(int i=1;i<digits.length();++i){
		if(digits[i-1]>digits[i])
			return false;
	}
	return true;
}
void count(int base, int size, int max, int j){
	for(int i=max;i>=0;i--){
		string res=int_to_str(i);
		if(isAscending(res)){
			cout<<"Case #"<<j<<": "<<res<<endl;
			return ;
		}
	}
}
int main(){
	FILE *fp;
	fp=fopen("B-small-attempt0.in","r");
	int t;
	fscanf(fp,"%d",&t);
	for(int j=1;j<=t;j++){
		int max,digits;
		fscanf(fp,"%d",&max);
		if(max<10)
			digits=1;
		else if(max<100)
			digits=2;
		else if(max<1000)
			digits=1;
		count(10, digits,max,j);
	}
}
