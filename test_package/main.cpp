#include <iostream>
#include <igtl/igtlOSUtil.h>

int main(int argc, char* argv[])
{
  int interval = 1000;
  igtl::Sleep(interval);

  std::cout << "SUCCESS" << std::endl;

  return EXIT_SUCCESS;
}
