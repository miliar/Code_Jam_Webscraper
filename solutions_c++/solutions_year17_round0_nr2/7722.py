#include <fstream>
#include <cstdio>
#include <string>
#include <sstream>
#include <iostream>


using namespace std;

int main(int argc, char **argv)
{
    ifstream input("B-large.in",ios::in);
    ofstream output("B-large.out", ios::out);

	//number of test cases
	int t;
	int cas;

	string N;
    string Y;

    int it;
    int Nsize;
    bool asc;
    char prev;

    int i;
    int start;

	input>>t;

	for(cas=0; cas<t; ++cas){

        input>>N;
        Nsize = N.size();
        asc = true;
        prev = '0';
        it=0;
        start=0;

        string Y(N);

        while(it<Nsize && asc==true){
            //ASCII comparison
            if(N[it]<prev){
                //1st digit is not 0
                if(prev=='1'){
                    Y[0]='0';
                    for(i=1;i<Nsize;i++){
                        Y[i]='9';
                    }
                }
                else{
                    Y[start]=(char)(prev-1);
                    for(i=start+1;i<Nsize;i++){
                        Y[i]='9';
                    }
                }
                asc=false;
            }
            else{
                if(N[it]>prev){
                    start=it;
                }
                prev = N[it];
                it++;
            }
        }

        if(Y[0]=='0'){
            Y=string(Y,1,Nsize);
        }


		output<<"Case #"<<(cas+1)<<": ";
		output<<Y<<endl;

	}

	return 0;
}
