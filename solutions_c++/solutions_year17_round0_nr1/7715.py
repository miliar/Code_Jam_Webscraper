#include <fstream>
#include <cstdio>
#include <string>
#include <sstream>
#include <iostream>


using namespace std;

int main(int argc, char **argv)
{
    ifstream input("A-large.in",ios::in);
    ofstream output("output_large.out", ios::out);

	//number of test cases
	int t;
	int cas;

	string faces;
	int k;
	int sizefaces;
	int nbflips;
	bool possible;


	int i;

	input>>t;

	for(cas=0; cas<t; ++cas){

        //cout<<cas;

		input>>faces>>k;
		sizefaces = faces.size();
		nbflips = 0;
		possible = true;

		int it = 0;
		while (it<sizefaces){
			if(faces[it]=='-'){
				if(it>sizefaces-k){
					possible=false;
				}
				else{
                    nbflips++;
					for(i=it;i<it+k;i++){
						if(faces[i]=='-')
							faces[i]='+';
						else faces[i]='-';
					}
				}
			}
        it++;
		}

		output<<"Case #"<<(cas+1)<<": ";
		if(possible==false)
			output<<"IMPOSSIBLE"<<endl;
		else
			output<<nbflips<<endl;


	}

	return 0;
}
