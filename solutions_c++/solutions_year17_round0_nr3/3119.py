// Created by Leonardo de Oliveira Ramos

#include <iostream>
#include <queue>
#define VECTOR_SIZE 4

using namespace std;

typedef struct stalls
{
	unsigned long int stall;
	unsigned long int quantity;
}stalls;

int main ()
{
	unsigned long int num_of_cases;

	cin >> num_of_cases;

	for (unsigned long int i = 0; i < num_of_cases; i++)
	{
		unsigned long int num_of_people;
		unsigned long int num_of_stalls;

		cin >> num_of_stalls >> num_of_people;
		
		stalls stall_groups[VECTOR_SIZE];

		for (unsigned long int j = 1; j < VECTOR_SIZE; j++)
		{
			stall_groups[j].stall = 0;
			stall_groups[j].quantity = 0;
		}
		stall_groups[0].stall = num_of_stalls;
		stall_groups[0].quantity = 1;


		for (unsigned long int j = 0; j < num_of_people;)
		{
			// Finding a valid bigger stall
			unsigned long int bigger_stall = -1;
			for (unsigned long int k = 0; k < VECTOR_SIZE && bigger_stall == -1; k++)
				if (stall_groups[k].quantity != 0)
					bigger_stall = k;

			// Finding the bigger stall
			for(unsigned long int k = 0; k < VECTOR_SIZE; k++)
				if ((stall_groups[k].quantity != 0) && stall_groups[k].stall > stall_groups[bigger_stall].stall)
					bigger_stall = k;

			// right/left stall is how many stalls is on the right/left of the "inserted" human
			unsigned long int right_stall = (stall_groups[bigger_stall].stall -1)/2;
			unsigned long int left_stall = stall_groups[bigger_stall].stall -1 -right_stall;

			// How many humans have those many empty stalls by their side
			unsigned long int divs;
			if (stall_groups[bigger_stall].quantity < (num_of_people - j))
				divs = stall_groups[bigger_stall].quantity;
			else
				divs = num_of_people - j;

			// iteration step
			j += divs;
			
			// output
			if (j >= num_of_people)
				cout << "Case #" << i+1 << ": " << left_stall << " " << right_stall << endl;
		
			// Now the bigger stall is split divs times
			stall_groups[bigger_stall].quantity -= divs;

			// 
			// INSERTING HUMAN(S)
			// 
			// Insert right_stall if already in stall_groups[]
			unsigned long int inserted1 = 0;
			unsigned long int inserted2 = 0;
			for (unsigned long int k = 0; k < VECTOR_SIZE && inserted1 == 0; k++)
			{
				if (stall_groups[k].stall == right_stall)
				{
					stall_groups[k].quantity += divs;
					inserted1 = 1;
				}
			}

			// Insert right_stall in case that is not already inserted
			for (unsigned long int k = 0; k < VECTOR_SIZE && inserted1 == 0; k++)
			{
				if (stall_groups[k].quantity == 0)
				{
					stall_groups[k].stall = right_stall;
					stall_groups[k].quantity = divs;
					inserted1 = 1;
				}
			}

			// Insert left_stall if already in stall_groups[]
			for (unsigned long int k = 0; k < VECTOR_SIZE && inserted2 == 0; k++)
			{
				if(stall_groups[k].stall == left_stall)
				{
					stall_groups[k].quantity += divs;
					inserted2 = 1;
				}
			}

			// Insert left_stall in case that is not already inserted
			for (unsigned long int k = 0; k < VECTOR_SIZE && inserted2 == 0; k++)
			{
				if (stall_groups[k].quantity == 0)
				{
					stall_groups[k].stall = left_stall;
					stall_groups[k].quantity = divs;
					inserted2 = 1;
				}
			}
		}
		

	}
}