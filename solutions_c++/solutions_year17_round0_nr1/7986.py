#include <iostream>
#include <fstream>
#include <string>

int main(int argc, char *argv[])
{
  if (argc != 2)
    return 1;
  std::ifstream file_in;
  std::ofstream file_out("output.out");
  std::string token;
  file_in.open(argv[1]);
  file_in >> token;
  int t = std::stoi(token);
  for (int row_idx = 1; row_idx <= t; row_idx++)
    {
      std::string str;
      file_in >> str;
      std::size_t len = str.size();
      file_in >> token;
      std::size_t k = std::stoi(token);
      // BEGIN
      std::size_t i = 0;
      int nb_moves = 0;
      while (i < len)
	{
	  if (str[i] == '-')
	    {
	      if (i + k <= len)
		{
		  for (std::size_t j = i; j < i + k; j++)
		    str[j] = (str[j] == '-') ? '+' : '-';
		  nb_moves++;
		}
	      else
		break;
	    }
	  i++;
	}
      file_out << "Case #" << row_idx << ": ";
      if (i >= len)
	file_out << nb_moves;
      else
	file_out << "IMPOSSIBLE";
      file_out << std::endl;
      // END
    }
  file_in.close();
  file_out.close();
  return 0;
}
