#include <iostream>
#include <string>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

struct number_s{
	unsigned long long number;
	unsigned long long amount;
};

int main()
{
	int numbers;
	
	cin >> numbers;
	
	
	
	for(int i = 1;i <= numbers;i++){
		
		unsigned long long rooms,people,actualP,answer;
		vector<number_s>tree;
		number_s temp,actualN;
		
		cin >> rooms >> people;
		
		actualP = 0;
		
		temp.number =  rooms;
		temp.amount = 1;
		tree.push_back(temp);
		
		while(actualP < people){
			
			actualP += tree.front().amount;
			
			if(people <= actualP){
				
				answer = tree.front().number;
				
				if(answer % 2 == 0)
				cout << "Case #" << i << ": " << answer / 2 << " " << answer / 2 - 1 << endl;
				else
				cout << "Case #" << i << ": " << answer / 2 << " " << answer / 2<< endl;
				
				break;
			}
			else{
				
				bool found;
				
				actualN = tree.front();
			//	cerr << "NUMBER "<< actualN.number << endl;
				
				if((actualN.number > 1)&&(actualN.number % 2 == 1)){
					
					found = 0;
					
					temp.amount = actualN.amount * 2;
					temp.number = actualN.number / 2;
					
					for(int j = 0;j < tree.size();j++){
				
						if(tree[j].number == temp.number){
							tree[j].amount += temp.amount;
							found = 1;
							
						//	cerr << "ALREADY EXISTS" << endl;
						}
					}
					
					if(found == 0){
						
						tree.push_back(temp);
						
						//cerr << temp.number << " "<< temp.number << endl;
						
					}
				}
				else{
					
					found = 0;
					
					temp.amount = actualN.amount;
					temp.number = actualN.number / 2;
					
					
					for(int j = 0;j < tree.size();j++){
				
						if(tree[j].number == temp.number){
							tree[j].amount += temp.amount;
							found = 1;
							//	cerr << "ALREADY EXISTS" << endl;
						}
					}
					
					if(found == 0){
						
						tree.push_back(temp);
						//cerr << temp.number << " ";
						
					}
					
					
					found = 0;
					
					temp.number -= 1;
					
					if(temp.number > 0){
					
						for(int j = 0;j < tree.size();j++){
					
							if(tree[j].number == temp.number){
								tree[j].amount += temp.amount;
								found = 1;
								
								//	cerr << "ALREADY EXISTS" << endl;
							}
						}
						
						if(found == 0){
							
							tree.push_back(temp);
							//cerr << temp.number << endl;
							
						}
						
					}
				}
				
				
			}
			
			tree.erase(tree.begin());
	
		//	system("pause");
		}
		
		
	
	}
	
	

		

}
