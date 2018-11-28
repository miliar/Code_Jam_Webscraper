#include <fstream>
#include <string>
#include <iostream>
#include <vector>

bool es_trie(std::vector<int> tab){
	for (int i = 0; i < tab.size()-1; i++)
		if (tab[i]<tab[i+1])
			return false;
	return true;
}

std::vector<int> make_tab(long number){
		long numberForDigitCalculation1, numberForMakeTab1;
		int nbDigits=0;
		int base=10;
		int test=0;
		std::vector<int> tabInt;

		numberForDigitCalculation1 = number;
		do{
			nbDigits+=1;
			numberForDigitCalculation1 /= 10;
		}while(numberForDigitCalculation1);


		numberForMakeTab1 = number;
		for (int i = 0; i < nbDigits; i++)
		{
			tabInt.push_back((numberForMakeTab1%base-test)/(base/10));
			test = numberForMakeTab1%base;
			base*=10;
		}
		return tabInt;
}

int main(int argc, char const *argcv[])
{
	long number;
	int cases;
	int cas_traite=1;
	std::vector<int> tabInt;

	std::ifstream infile("input.txt");
	std::ofstream fout("output.txt");

	//recupère le nombre de cas
	infile >> cases;

	// traite cas par

	while(cas_traite <= cases && infile >> number){	
		//get number of digit of number input
		tabInt = make_tab(number);
		if(es_trie(tabInt)){
			fout<<"Case #"<< cas_traite << ": " << number << std::endl;
		}else{
			do{
				tabInt = make_tab(--number);
			}while(!es_trie(tabInt));

			fout<<"Case #"<< cas_traite << ": " << number << std::endl;
		}
		cas_traite++;
		
	}
	return 0;
}