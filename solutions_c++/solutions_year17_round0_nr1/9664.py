

#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>

using namespace std;
ifstream in;
ofstream out;

int getMinFlip(string pancake, int K){
	int end=pancake.size()-1;
	int Pancakesize = pancake.size()-1;
	int start = 0;
	int counter = 0;
	//while(start < end){
	while(1){
		//while(pancake[start]=='+' && start < end ){
		while(pancake[start]=='+' && start < Pancakesize){
			start++;
		}
		while(pancake[end]=='+' && 0 < end ){
			end--;
		}
		if(start > end){
			return counter;
		} else if( end-start < (K-1) ){
			return (-1);
		} else {
			for(int i=0;i<K;i++) {
				//if(start+i<=end){
					if(pancake[start+i]=='-'){
						pancake[start+i]='+';
					}else{
						pancake[start+i]='-';
					}
				//}
				//else{
					//return (-1);
				//}
			}
			
			counter++;
		}


		while(pancake[start]=='+' && start < Pancakesize ){
			start++;
		}
		while(pancake[end]=='+' && 0 < end ){
			end--;
		}
		
		if(start > end){
			return counter;
		} else if( (end-start) < (K-1) ){
			return (-1);
		} else {
			for(int i=0;i<K;i++) {
				//if(end-i>=start){
					if(pancake[end-i]=='-'){
						pancake[end-i]='+';
					}else{
						pancake[end-i]='-';
					}
				//} else{
					//return (-1);
				//}
			}
			counter++;
		}
		//start++;
		//end--;
	}
}

void PrintResult(int caseid, int fliptime)
{
	if(fliptime!=-1){
		out<<"Case #"<<caseid+1<<": "<<fliptime<<endl;
	} else{
		out<<"Case #"<<caseid+1<<": "<<"IMPOSSIBLE"<<endl;
	}
		
}

/*
double GiveTime(double C, double F, double X )
{
	double Time=0.00;
	double i=0.0;
	while(X/(2+F*i)>C/(2+F*i)+X/(2+F*(i+1)))
	{i=i+1;}
	double m=i;
	for(int k=0;k<m;k++)
	{
	Time=Time+C/(2+k*F);
	}
	Time=Time+X/(2+F*m);
	return Time;

}

void PrintResult(int caseid,double time)
{
	out<<"Case #"<<caseid+1<<": "<<setprecision(14)<<fixed<<time<<endl;

}
*/
int main()
{

   in.open("A-large (2).in");
   out.open("A-large (2).out");
   if(!in) {
		cout<<"no A-small-attempt0.in available!"<<endl;
		system("pause");
   }
   int caseNUM;
   
   in>>caseNUM;
   
   //float currentC,currentF,currentX=0.0;
   string pancakeSeries;
   int panSize;
   for(int i=0;i<caseNUM;i++)
   {
	   //in my code C and F and the other way round;
	   //in>>currentC>>currentF>>currentX;
	   in>>pancakeSeries>>panSize;
	   int indResult = getMinFlip(pancakeSeries,panSize);
	   //PrintResult(i,GiveTime(currentC,currentF,currentX));
	   PrintResult(i,indResult);
   }

   out.close();
   in.close();
   
   return 0;
}
   