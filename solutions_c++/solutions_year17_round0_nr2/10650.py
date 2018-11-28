		#include <iostream>
		#include <vector>
		#include <set>
		#include <fstream>
		
		void print_each_digit(int x, std::vector<int> &v);
		
		int main()
		{
			
			int testCase = 1;
			int N		 = 0;
			unsigned int K = 0;
			
			    std::ofstream outfile;
    			outfile.open("output.txt");
   				 //std::ifstream infile("A-small-practice.in");
				std::ifstream infile("B-small-attempt1.in");


			infile >> N;		
			//std::cin >> N;
			
			while(N--)
			{
			
				infile >> K;
				//std::cin >> K;
				bool foundNumber = false;
				unsigned int tidy = 0;
				
				do
				{
					std::vector<int> v;
					v.clear();
				
					print_each_digit(K, v);
				
					std::vector<int>::iterator it;
					it = v.begin();
				
					bool isTidy = true;
				
					for(it = v.begin(); it != v.end(); it++)
					{				
						if(it != v.begin())
						{
							int temp = *(std::prev(it,1));
							if(temp > *it)
							{
								isTidy = false;
								break;
							}
						}
					}
					
					if(isTidy)
					{
						tidy = K;
						break;
					}
					
						
					K--;
				}	
				while(K != 0 || !foundNumber);
	
				
									
				//std::cout << "Case #" << testCase << ": " << tidy << std::endl;
				outfile << "Case #" << testCase << ": " << tidy << std::endl;
	
			
				testCase++;
			}
			
			outfile.close();
			return 0;
		}
		
		
		
		void print_each_digit(int x, std::vector<int> & v)
		{
		    if(x >= 10)
		       print_each_digit(x / 10,  v);
		
		    int digit = x % 10;
		    v.push_back(digit);
		};
		
		

