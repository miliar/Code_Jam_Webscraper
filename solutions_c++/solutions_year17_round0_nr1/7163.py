// g++ largePancake.cpp -o largePancake && ./largePancake < test.txt
#include <iostream>
#include <string>

int main(int argc, char **argv){
	int T,K;
	std::string S;
	bool *pancakes; //true indicate a pancake with the happy side up
	bool allHappy;
	
	std::cin >> T;
	for(int i=1; i<T+1; i++){
		std::cin >> S;
		std::cin >> K;
		int Slength = S.length();
		pancakes = new bool[Slength];
		for(int j=0; j<Slength; j++){
			if(S[j] == '+')
				pancakes[j] = true;
			else
				pancakes[j] = false;
		}
		int flips = 0;
		for (int j=0; j<=Slength-K; j++){
			if(!pancakes[j]){
				flips++;
				for(int h=0; h<K; h++)
					pancakes[j+h] = !pancakes[j+h];
			}
		}
		allHappy = true;
		for(int j=Slength-K+1; j<Slength; j++)
			if(!pancakes[j]){
				allHappy = false;
				break;
			}
		if(allHappy)
			std::cout << "Case #" << i << ": " << flips << std::endl;
		else
			std::cout << "Case #" << i << ": " << "IMPOSSIBLE" << std::endl;
		
		//std::cout << "S = " << S << " ::: S.length() = " << S.length() << " ::: K = " << K << std::endl;
		//std::cout << "S = ";
		//for (int j=0; j<Slength; j++)
			//std::cout << pancakes[j];
		//std::cout << std::endl;
		delete[] pancakes;
	}
	
	return 0;
}
